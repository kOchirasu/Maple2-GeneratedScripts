using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001483: Mue
/// </summary>
public class _11001483 : NpcScript {
    internal _11001483(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0106111607005777$ 
                // - What brings you here?
                return true;
            case 30:
                // $script:0106111607005780$ 
                // - Ooh... This temple creeps me out. I can't find anyone in this gloomy place...
                // $script:0106111607005781$ 
                // - D-do you see the door over there? I think something awful happened on the other side... I'm scared...
                return true;
            default:
                return true;
        }
    }
}
