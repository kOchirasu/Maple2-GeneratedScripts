using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001691: Warehouse Computer
/// </summary>
public class _11001691 : NpcScript {
    internal _11001691(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0629000607006500$ 
                // - Connecting to the BeyondLink database...
                return true;
            case 10:
                // $script:0705132707006616$ 
                // - Verifying data access credentials...
                //   Connecting to the BeyondLink database...
                switch (selection) {
                    // $script:0705132707006617$
                    // - (View Code 0.)
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0705132707006618$ 
                // - Accessing Code 0...
                //   An error has occurred. You do not have permission to access Code 0 Mantra.
                switch (selection) {
                    // $script:0705132707006619$
                    // - (View Code 2.)
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0705132707006620$ 
                // - Your request to access Code 2 Katramus has been denied.
                //   Your code key has expired.
                return true;
            default:
                return true;
        }
    }
}
