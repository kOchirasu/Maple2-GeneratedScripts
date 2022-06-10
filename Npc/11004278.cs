using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004278: Shadow Dragon Statue
/// </summary>
public class _11004278 : NpcScript {
    internal _11004278(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011283$ 
                // - <font color="#909090">(You feel an ominous chill as you gaze upon the dragon statue.)</font> 
                return true;
            case 10:
                // $script:0911203207011284$ 
                // - <font color="#909090">(You feel an ominous chill as you gaze upon the dragon statue.)</font> 
                // $script:0911203207011285$ 
                // - <font color="#909090">(This statue was once a grand piece of architecture, proudly displaying the spirit of the dragons. However, it's been altered by darkness.)</font> 
                // $script:0911203207011286$ 
                // - <font color="#909090">(The power of the dragons of light which once protected Nazkar is completely gone. Now, all avoid this once-sacred area.)</font> 
                return true;
            default:
                return true;
        }
    }
}
