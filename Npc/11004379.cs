using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004379: Maximilian
/// </summary>
public class _11004379 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;40
    }

    // Select 0:
    // $script:1109213607011793$
    // - I'll be honest, I didn't think this place was so merry until <i>you</i> showed up.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011794$
                // - I'll be honest, I didn't think this place was so merry until <i>you</i> showed up.
                return -1;
            case (40, 0):
                // $script:1120173007011868$
                // - I'll be honest, I didn't think this place was so merry until <i>you</i> showed up.
                switch (selection) {
                    // $script:1120173007011869$
                    // - Did you see $npcName:11004345[gender:1]$'s family?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1120173007011870$
                // - $npcName:11004345[gender:1]$? That's $npcName:11004347[gender:1]$'s daughter. She's my boss, but she's off today. You sure she's not at home?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
