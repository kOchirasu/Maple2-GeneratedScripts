using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003102: SwolePatrol Guild Leader
/// </summary>
public class _11003102 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0119135307007835$
    // - Hm, you look like you could use some exercise.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0119135307007838$
                // - Isn't it time you got buff? I'd invite you to my SwolePatrol guild but we don't have any openings. 
                switch (selection) {
                    // $script:0119135307007839$
                    // - I totally want to join your guild!
                    case 0:
                        return 31;
                    // $script:0119135307007840$
                    // - Not really my scene, but thanks.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0119135307007841$
                // - What's wrong, got fries in your ears? Just kidding, but for real we're full. You're gonna have to find another guild to pump you up.
                return -1;
            case (32, 0):
                // $script:0119135307007842$
                // - Oh, really? I have a feeling you'll be changing your mind sometime soon. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
