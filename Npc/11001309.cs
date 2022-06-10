using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001309: Devin
/// </summary>
public class _11001309 : NpcScript {
    internal _11001309(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005028$ 
                // - Ugh, my head...
                return true;
            case 40:
                // $script:1227194507005659$ 
                // - I've got more cases on my plate than I could ever solve in a single lifetime.
                // $script:1227194507005660$ 
                // - Sure, I'm happy that $map:02010002$ is growing. But does the crime have to grow with it? Our prison is bursting at the seams!
                // $script:1227194507005661$ 
                // - This isn't police work. It's war! But somebody's got to protect the city, right?
                return true;
            default:
                return true;
        }
    }
}
