using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001631: Bravos
/// </summary>
public class _11001631 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0516130207006133$
    // - Cut to the chase.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0629205207006505$
                // - The moment you step out of here, you're a marked $male:man,female:woman$. Capisce?
                switch (selection) {
                    // $script:0629205207006506$
                    // - I have no clue what you're talking about.
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:0629205207006507$
                // - That's fine. You go about your business. You leave the thinking to me.
                return 30;
            case (30, 1):
                // $script:0630212007006533$
                // - You better be careful. We're watching you.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
