using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004221: Agent S
/// </summary>
public class _11004221 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806222707010788$
    // - I can't really talk right now.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806222707010789$
                // - Can't talk, secret mission. I told $npc:11004220[gender:0]$ to meet right here by the balloons. Where is he? You don't think <i>they</i> got to him first, do you...?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
