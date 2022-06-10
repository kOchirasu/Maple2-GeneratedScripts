using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004074: Overheating Dog
/// </summary>
public class _11004074 : NpcScript {
    internal _11004074(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010189$ 
                // - Ah, it's hot... Even hotter than yesterday... 
                return true;
            case 10:
                // $script:0619202207010190$ 
                // - Ah, it's hot... Even hotter than yesterday... 
                // $script:0619202207010191$ 
                // - <i>Another</i> human? Phew. You guys really don't mind this heat? 
                switch (selection) {
                    // $script:0619202207010192$
                    // - What's the matter?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0619202207010193$ 
                // - Don't laugh! I've got heatstroke. I think. I came up here because it's cooler, and now I can't go back down because it's too hot. 
                switch (selection) {
                    // $script:0619202207010194$
                    // - You... do realize you're a fire dog, right?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0619202207010195$ 
                // - You think I don't know how weird it is that I hate the heat? Maybe it's because I was born in winter... 
                switch (selection) {
                    // $script:0619202207010196$
                    // - I thought you guys needed fire to stay alive.
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0619202207010197$ 
                // - No, no more fire! I can't go back down there. I gotta shake this heatstroke... 
                switch (selection) {
                    // $script:0619202207010198$
                    // - Eating something spicy might take your mind off the heat.
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:0619202207010199$ 
                // - You're just like all those people napping down there. No help. No help at all... 
                return true;
            default:
                return true;
        }
    }
}
