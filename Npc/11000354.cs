using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000354: Chairman Goldus
/// </summary>
public class _11000354 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50
    }

    // Select 0:
    // $script:0831180407001472$
    // - Grr...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001475$
                // - Ah, I'm finally safe! You're my savior.
                return -1;
            case (40, 0):
                // $script:0831180407001476$
                // - I thought I was going to die. I used to think I was untouchable. But after they took me so easily...
                return -1;
            case (50, 0):
                // $script:0831180407001477$
                // - I can't believe you came to save me... Thank you. I'll live an honest life from now on. I'll donate to charities, pay all my taxes, and volunteer at the soup kitchens.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
