using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001714: Tinchai
/// </summary>
public class _11001714 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006966$
    // - Hello there.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0805021607007090$
                // - None of us are okay right now. All the more reason to stay strong.
                switch (selection) {
                    // $script:0805021607007091$
                    // - (Nod your head.)
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0805021607007092$
                // - You know, I... Oh, never mind.
                //   <font color="#909090">($npcName:11001714[gender:1]$ looks you in the eye, but stops herself from saying more.)</font>
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
