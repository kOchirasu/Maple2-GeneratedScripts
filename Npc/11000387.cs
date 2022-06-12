using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000387: May
/// </summary>
public class _11000387 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001574$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001576$
                // - Have you seen $npcName:11000406[gender:0]$? He's right over there... and he's sooooooo handsome. Ah, I wish I could get close to him...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
