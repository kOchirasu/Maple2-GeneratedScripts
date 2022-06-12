using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001656: Tinchai
/// </summary>
public class _11001656 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0617105607006366$
    // - Halo Mountain...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0727223007006860$
                // - We need to focus... focus...
                switch (selection) {
                    // $script:0727223007006861$
                    // - Is the master really gone?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0727223007006862$
                // - <font color="#909090">($npcName:11001656[gender:1]$ chokes back a tear.)</font>
                //   The master is fine. He... he has to be...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
