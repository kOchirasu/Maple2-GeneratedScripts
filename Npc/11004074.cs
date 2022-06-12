using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004074: Overheating Dog
/// </summary>
public class _11004074 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010189$
    // - Ah, it's hot... Even hotter than yesterday...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010190$
                // - Ah, it's hot... Even hotter than yesterday...
                return 10;
            case (10, 1):
                // $script:0619202207010191$
                // - <i>Another</i> human? Phew. You guys really don't mind this heat?
                switch (selection) {
                    // $script:0619202207010192$
                    // - What's the matter?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0619202207010193$
                // - Don't laugh! I've got heatstroke. I think. I came up here because it's cooler, and now I can't go back down because it's too hot.
                switch (selection) {
                    // $script:0619202207010194$
                    // - You... do realize you're a fire dog, right?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0619202207010195$
                // - You think I don't know how weird it is that I hate the heat? Maybe it's because I was born in winter...
                switch (selection) {
                    // $script:0619202207010196$
                    // - I thought you guys needed fire to stay alive.
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0619202207010197$
                // - No, no more fire! I can't go back down there. I gotta shake this heatstroke...
                switch (selection) {
                    // $script:0619202207010198$
                    // - Eating something spicy might take your mind off the heat.
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:0619202207010199$
                // - You're just like all those people napping down there. No help. No help at all...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
