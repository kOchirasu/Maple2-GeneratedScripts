using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001691: Warehouse Computer
/// </summary>
public class _11001691 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0629000607006500$
    // - Connecting to the BeyondLink database...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0705132707006616$
                // - Verifying data access credentials...
                //   Connecting to the BeyondLink database...
                switch (selection) {
                    // $script:0705132707006617$
                    // - (View Code 0.)
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0705132707006618$
                // - Accessing Code 0...
                //   An error has occurred. You do not have permission to access Code 0 Mantra.
                switch (selection) {
                    // $script:0705132707006619$
                    // - (View Code 2.)
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0705132707006620$
                // - Your request to access Code 2 Katramus has been denied.
                //   Your code key has expired.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
