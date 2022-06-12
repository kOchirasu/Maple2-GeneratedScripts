using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004493: Bacopa
/// </summary>
public class _11004493 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012347$
    // - I'm here researching the fish of Kritias.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012348$
                // - I'm here researching the fish of Kritias.
                switch (selection) {
                    // $script:1227192907012349$
                    // - What have you learned?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012350$
                // - Every fish I've caught has had trace amounts of aetherine in their systems. The amount might be related to their place in the food chain...
                return 11;
            case (11, 1):
                // $script:1227192907012351$
                // - If I were to cook and eat one of these fish, would the aetherine stay in <i>my</i> system? Until I figure this out, we're going to be reliant on food rations delivered from the mainland.
                switch (selection) {
                    // $script:0114161207012703$
                    // - I hope you figure it out.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0114161207012704$
                // - So do I, my friend. So do I.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
