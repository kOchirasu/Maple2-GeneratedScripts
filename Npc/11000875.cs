using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000875: Brynner
/// </summary>
public class _11000875 : NpcScript {
    internal _11000875(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003181$ 
                // - I'm going to be rich soon.
                return true;
            case 20:
                // $script:0831180407003183$ 
                // - What am I going to do when I become rich? Well... I want a nice-looking house, a nice-looking car, nice-looking clothes, nice-looking shoes... Basically, everything I have should look nice. Right?
                return true;
            default:
                return true;
        }
    }
}
