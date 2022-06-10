using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004510: Mannstad Patrolman
/// </summary>
public class _11004510 : NpcScript {
    internal _11004510(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228182607012457$ 
                // - What're you, a tourist? You wanna get tombstoned? This is a warzone! Not that $map:02020030$ is any better...
                return true;
            case 10:
                // $script:1228182607012458$ 
                // - What're you, a tourist? You wanna get tombstoned? This is a warzone! Not that $map:02020030$ is any better...
                return true;
            default:
                return true;
        }
    }
}
