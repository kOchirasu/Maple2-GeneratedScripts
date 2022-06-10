using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001062: Nox
/// </summary>
public class _11001062 : NpcScript {
    internal _11001062(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180306000378$ 
                // - You must be here to see me.
                return true;
            case 40:
                // $script:1208032606000568$ 
                // - Mm? Is there something you'd like to trade?
                switch (selection) {
                    // $script:1208032606000569$
                    // - I heard you collect $itemPlural:40100024$.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1208032606000570$ 
                // - You're pretty lucky if you find $itemPlural:40100024$, but I can't help you. I'm actually out of business. If you want to buy items, you'll have to shop elsewhere.
                switch (selection) {
                    // $script:1208032606000571$
                    // - You're out of business?!
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1208032606000572$ 
                // - Why does any businessman go out of business? I'm not making enough profit.
                // $script:1208032606000573$ 
                // - I'll either have to start selling different products or stop selling altogether...
                return true;
            default:
                return true;
        }
    }
}
