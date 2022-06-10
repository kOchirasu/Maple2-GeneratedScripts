using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004494: Pusilla
/// </summary>
public class _11004494 : NpcScript {
    internal _11004494(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012354$ 
                // - This place was a dense forest when we first got here...
                return true;
            case 10:
                // $script:1227192907012355$ 
                // - This place was a dense forest when we first got here...
                switch (selection) {
                    // $script:1227192907012356$
                    // - What happened?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012357$ 
                // - We set up camp just a day after the Daemon Army arrived. This is all that's left of the forest. The stream is totally dead now, too.
                // $script:1227192907012358$ 
                // - We've seen this kind of rapid transformation before. In the Land of Darkness...
                // $script:1227192907012359$ 
                // - As the Daemon Army expands, this massive die-off of nature will follow.
                switch (selection) {
                    // $script:0114164507012725$
                    // - That's bad news.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0114164607012725$ 
                // - We need to stop them before they spread any further.
                return true;
            default:
                return true;
        }
    }
}
