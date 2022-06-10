using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000241: Sally
/// </summary>
public class _11000241 : NpcScript {
    internal _11000241(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001019$ 
                // - Welcome.
                return true;
            case 20:
                // $script:0831180407001021$ 
                // - Are you heading to $map:02000135$? It's famous for its beautiful scenery. At the very top you'll find the Cloud Cafe, famous among young couples. You can take the cable car all the way up to the top if you want to see it.
                // $script:0831180407001022$ 
                // - Our cable cars are made to last. They won't break, no matter how hard you jump! Please note that we won't be liable for injuries if you jump yourself right out of the car.
                return true;
            default:
                return true;
        }
    }
}
