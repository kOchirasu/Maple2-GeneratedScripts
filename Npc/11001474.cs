using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001474: Fabid
/// </summary>
public class _11001474 : NpcScript {
    internal _11001474(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1224110207005585$ 
                // - W-what?
                return true;
            case 30:
                // $script:1228134707005721$ 
                // - M-m-must stay calm. I'm n-n-not scared...
                switch (selection) {
                    // $script:0913170607011310$
                    // - What's wrong?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0913170607011311$ 
                // - <b>AH!!</b> Jeez, you almost gave me a heart attack...
                // $script:0913170607011312$ 
                // - You aren't headed into the $dungeonTitle:20016002$, are you? I was researching the ruins there when I saw... one of "them!"
                // $script:0913170607011313$ 
                // - How did the temple of the divine lumarigons come to house such frightening creatures? It's enough to make a man quake in his boots.
                return true;
            default:
                return true;
        }
    }
}
