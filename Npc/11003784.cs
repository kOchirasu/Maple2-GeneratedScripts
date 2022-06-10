using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003784: Veliche
/// </summary>
public class _11003784 : NpcScript {
    internal _11003784(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213192607009638$ 
                // - Need something? 
                return true;
            case 10:
                // $script:1213192607009639$ 
                // - The future is in our hands. 
                return true;
            case 20:
                // $script:0131125107009814$ 
                // - Need something? 
                // $script:0131125107009815$ 
                // - It seems you came up to keep us supplied.
There's no time to waste. Head to <font color="#ffd200">$map:52010063$</font> right away. 
                // $script:0131125107009817$ functionID=1 
                // - I'll arrange a transport for you. 
                return true;
            case 30:
                // $script:0131125107009816$ 
                // - The future is in our hands. 
                return true;
            default:
                return true;
        }
    }
}
