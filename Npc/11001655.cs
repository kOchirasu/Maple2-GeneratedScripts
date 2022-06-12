using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001655: Tinchai
/// </summary>
public class _11001655 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0617105607006365$
    // - Where did $npcName:11001557[gender:0]$ get off to...?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0727223007006855$
                // - Did you see that shadow? I wonder if that was $npcName:11001557[gender:0]$ skulking around.
                switch (selection) {
                    // $script:0727223007006856$
                    // - I didn't see anything.
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0727223007006857$
                // - Well, I know I saw something! And he has to be around here somewhere.
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
