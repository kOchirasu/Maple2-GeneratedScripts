using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004313: Condor
/// </summary>
public class _11004313 : NpcScript {
    internal _11004313(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0928133807011352$ 
                // - Back in my day, we knew a thing or two about duty!
                return true;
            case 10:
                // $script:0928133807011353$ 
                // - I'm here, but most of my men are tied up defending Victoria Island. I hate being benched!
                return true;
            default:
                return true;
        }
    }
}
