using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004085: Oath Marker
/// </summary>
public class _11004085 : NpcScript {
    internal _11004085(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0622133907010290$ 
                // - <font color="#909090">(This enchanted marker has been warded against the ages. Ancient writing has been etched into it.)</font>
                return true;
            case 10:
                // $script:0622133907010291$ 
                // - <font color="#909090">(This enchanted marker has been warded against the ages. Ancient writing has been etched into it.)</font>
                // $script:0622133907010292$ 
                // - <i>When our world was young, the goddess of light faded away. It became the responsibility of us fairfolk to carry what remained of her work into the future.</i>
                // $script:0622133907010293$ 
                // - <i>The taint of the darkness remained. Without our goddess, it fell to us to seal it away.</i>
                // $script:0622133907010294$ 
                // - <i>Someday, we believe that our goddess will return to us in mortal form. Until then, we wait and stand watch against the shadows.</i>
                return true;
            default:
                return true;
        }
    }
}
