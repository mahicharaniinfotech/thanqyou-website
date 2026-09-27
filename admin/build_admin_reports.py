r"""
Adds a Reports page to the ThanQYou admin panel: pending post_reports
and user_reports, with Approve / Remove-post / Block-user actions.
Uses the existing query()/update()/deleteRow() helpers and the
is_blocked/social_blocked/block_reason columns already on
social_accounts (previously unused by any admin UI).

Usage:
    python build_admin_reports.py

Run from anywhere -- pass the admin index.html path as the only argument,
e.g.:
    python build_admin_reports.py "C:\Users\workw\Desktop\ThanQYou\admin\index.html"
"""

import sys
from pathlib import Path

def fail(msg):
    print(f"FAILED: {msg}")
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        fail("Usage: python build_admin_reports.py <path-to-index.html>")
    path = Path(sys.argv[1])
    if not path.exists():
        fail(f"{path} not found.")
    text = path.read_text(encoding="utf-8")

    if "page-reports" in text:
        print("SKIP: already patched.")
        return

    # 1. Nav item -- right after Content's nav-item.
    old_nav = (
        '    <div class="nav-item" onclick="showPage(\'content\',this)">\n'
        '      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>\n'
        '      Content\n'
        '    </div>'
    )
    if old_nav not in text:
        fail("Could not find the Content nav-item anchor.")
    new_nav = (
        old_nav
        + '\n    <div class="nav-item" onclick="showPage(\'reports\',this)">\n'
        + '      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>\n'
        + '      Reports\n'
        + '    </div>'
    )
    text = text.replace(old_nav, new_nav, 1)

    # 2. Page HTML -- inserted right before the Content page div.
    old_page_anchor = '    <div class="page" id="page-content">'
    if old_page_anchor not in text:
        fail("Could not find the page-content div anchor.")
    new_page_block = (
        '    <!-- REPORTS -->\n'
        '    <div class="page" id="page-reports">\n'
        '      <div class="stats-row">\n'
        '        <div class="mini-stat"><div class="ms-val" id="rp-pending-posts">\u2014</div><div class="ms-label">Pending Post Reports</div></div>\n'
        '        <div class="mini-stat"><div class="ms-val" id="rp-pending-users">\u2014</div><div class="ms-label">Pending User Reports</div></div>\n'
        '      </div>\n'
        '      <div class="panel">\n'
        '        <h3>Reported Posts</h3>\n'
        '        <table>\n'
        '          <thead><tr><th>Post</th><th>Post Author</th><th>Reported By</th><th>Reason</th><th>Date</th><th>Actions</th></tr></thead>\n'
        '          <tbody id="reports-post-body"><tr><td colspan="6"><div class="loading"><div class="spinner"></div></div></td></tr></tbody>\n'
        '        </table>\n'
        '      </div>\n'
        '      <div class="panel" style="margin-top:20px">\n'
        '        <h3>Reported Users</h3>\n'
        '        <table>\n'
        '          <thead><tr><th>Reported Account</th><th>Reported By</th><th>Reason</th><th>Date</th><th>Actions</th></tr></thead>\n'
        '          <tbody id="reports-user-body"><tr><td colspan="5"><div class="loading"><div class="spinner"></div></div></td></tr></tbody>\n'
        '        </table>\n'
        '      </div>\n'
        '    </div>\n\n'
        + old_page_anchor
    )
    text = text.replace(old_page_anchor, new_page_block, 1)

    # 3. pageTitles
    old_titles = "  dashboard:'Dashboard', users:'Users', content:'Content', kyc:'KYC Verification',"
    if old_titles not in text:
        fail("Could not find the pageTitles anchor.")
    new_titles = "  dashboard:'Dashboard', users:'Users', content:'Content', reports:'Reports', kyc:'KYC Verification',"
    text = text.replace(old_titles, new_titles, 1)

    # 4. loaders map, occurrence #1 (showPage)
    old_loaders1 = (
        "    dashboard: loadDashboard, users: loadUsers, content: loadContent,\n"
        "    kyc: loadKYC, wallet: loadWallet, referrals: loadReferrals, payouts: loadPayouts,"
    )
    if old_loaders1 not in text:
        fail("Could not find loaders map anchor #1 (showPage).")
    new_loaders1 = (
        "    dashboard: loadDashboard, users: loadUsers, content: loadContent, reports: loadReports,\n"
        "    kyc: loadKYC, wallet: loadWallet, referrals: loadReferrals, payouts: loadPayouts,"
    )
    text = text.replace(old_loaders1, new_loaders1, 1)

    # 5. loaders map, occurrence #2 (refreshCurrentPage) -- small,
    # unambiguous partial anchor since the full line is very long.
    old_loaders2 = "content:loadContent,kyc:loadKYC,wallet:loadWallet,referrals:loadReferral"
    if old_loaders2 not in text:
        fail("Could not find loaders map anchor #2 (refreshCurrentPage).")
    new_loaders2 = "content:loadContent,reports:loadReports,kyc:loadKYC,wallet:loadWallet,referrals:loadReferral"
    text = text.replace(old_loaders2, new_loaders2, 1)

    # 6. The JS functions themselves -- inserted right before deletePost,
    # reusing the exact same style (var, string concatenation) as the
    # surrounding code rather than mixing in modern syntax.
    old_delete_post = "async function deletePost(id){"
    if old_delete_post not in text:
        fail("Could not find deletePost anchor for function insertion.")
    new_functions = '''async function loadReports(){
  document.getElementById('reports-post-body').innerHTML='<tr><td colspan="6"><div class="loading"><div class="spinner"></div></div></td></tr>';
  document.getElementById('reports-user-body').innerHTML='<tr><td colspan="5"><div class="loading"><div class="spinner"></div></div></td></tr>';
  var res=await Promise.all([
    query('post_reports','select=*&status=eq.pending&order=created_at.desc'),
    query('user_reports','select=*&status=eq.pending&order=created_at.desc'),
    query('social_accounts','select=id,social_uid,username_handle,username,social_avatar_url')
  ]);
  var postReports=res[0]||[],userReports=res[1]||[];
  var accts={};(res[2]||[]).forEach(function(a){accts[a.social_uid]=a;});
  window._accts=accts;
  document.getElementById('rp-pending-posts').textContent=postReports.length;
  document.getElementById('rp-pending-users').textContent=userReports.length;

  var postIds=Array.from(new Set(postReports.map(function(r){return r.post_id;}).filter(Boolean)));
  var posts={};
  if(postIds.length){
    var fetched=await query('posts','select=id,caption,social_uid&id=in.('+postIds.join(',')+')');
    (fetched||[]).forEach(function(p){posts[p.id]=p;});
  }

  renderPostReports(postReports,posts);
  renderUserReports(userReports);
}
function nameFor(uid){
  var a=window._accts&&window._accts[uid];
  return a?('@'+(a.username_handle||a.username||uid.substring(0,8))):(uid?uid.substring(0,8):'\u2014');
}
function renderPostReports(reports,posts){
  var body=document.getElementById('reports-post-body');
  if(!reports.length){body.innerHTML='<tr><td colspan="6"><div class="empty-state"><p>No pending post reports</p></div></td></tr>';return;}
  body.innerHTML=reports.map(function(r){
    var p=posts[r.post_id];
    var caption=p?(p.caption||'(no caption)'):'(post already removed)';
    return '<tr>'
      +'<td style="font-size:12px;max-width:220px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">'+caption+'</td>'
      +'<td>'+(p?nameFor(p.social_uid):'\u2014')+'</td>'
      +'<td>'+nameFor(r.social_uid)+'</td>'
      +'<td><span class="badge badge-red">'+r.reason+'</span></td>'
      +'<td style="font-size:12px">'+formatDate(r.created_at)+'</td>'
      +'<td>'
        +'<button class="action-btn" onclick="resolveReport(\\'post_reports\\',\\''+r.id+'\\')">Approve (clean)</button> '
        +(p?'<button class="action-btn danger" onclick="removeReportedPost(\\''+r.id+'\\',\\''+r.post_id+'\\')">Remove post</button>':'')
      +'</td></tr>';
  }).join('');
}
function renderUserReports(reports){
  var body=document.getElementById('reports-user-body');
  if(!reports.length){body.innerHTML='<tr><td colspan="5"><div class="empty-state"><p>No pending user reports</p></div></td></tr>';return;}
  body.innerHTML=reports.map(function(r){
    return '<tr>'
      +'<td>'+nameFor(r.reported_social_uid)+'</td>'
      +'<td>'+nameFor(r.reporter_social_uid)+'</td>'
      +'<td><span class="badge badge-red">'+r.reason+'</span></td>'
      +'<td style="font-size:12px">'+formatDate(r.created_at)+'</td>'
      +'<td>'
        +'<button class="action-btn" onclick="resolveReport(\\'user_reports\\',\\''+r.id+'\\')">Approve (clean)</button> '
        +'<button class="action-btn danger" onclick="blockReportedUser(\\''+r.id+'\\',\\''+r.reported_social_uid+'\\')">Block user</button>'
      +'</td></tr>';
  }).join('');
}
async function resolveReport(table,id){
  var ok=await update(table,id,{status:'resolved'});
  if(ok){showToast('Marked as reviewed - clean');loadReports();}
  else showToast('Failed to update report','error');
}
async function removeReportedPost(reportId,postId){
  if(!confirm('Remove this post? This cannot be undone.'))return;
  var ok=await deleteRow('posts','id',postId);
  if(ok){
    await update('post_reports',reportId,{status:'resolved'});
    showToast('Post removed');
    loadReports();
  } else showToast('Failed to remove post','error');
}
async function blockReportedUser(reportId,socialUid){
  if(!confirm('Block this account? They will be removed from Social and unable to sign back in there.'))return;
  var acct=window._accts&&window._accts[socialUid];
  if(!acct||!acct.id){showToast('Account not found','error');return;}
  var ok=await update('social_accounts',acct.id,{is_blocked:true,social_blocked:true,block_reason:'Reported and reviewed by admin'});
  if(ok){
    await update('user_reports',reportId,{status:'resolved'});
    showToast('User blocked');
    loadReports();
  } else showToast('Failed to block user','error');
}
async function deletePost(id){'''
    text = text.replace(old_delete_post, new_functions, 1)

    path.write_text(text, encoding="utf-8", newline="\r\n")
    print(f"Patched: {path}")


if __name__ == "__main__":
    main()
