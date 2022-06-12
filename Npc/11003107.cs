using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003107: QuietMinds Guild Leader
/// </summary>
public class _11003107 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0119135307007855$
    // - There's nothing like a glass of something sweet to drink away your stress.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0119135307007858$
                // - Are you stressed out? I formed the QuietMinds guild to help people escape from the many stresses of life.
                switch (selection) {
                    // $script:0119135307007859$
                    // - I totally want to join your guild!
                    case 0:
                        return 31;
                    // $script:0119135307007860$
                    // - Not really my scene, but thanks.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0119135307007861$
                // - Oh! I'm sorry, but my guild is already full. Hm... Well, I'm sure I'm not the only one who formed a guild to relax. There has to be another chill guild somewhere. Or you could start your own.
                return -1;
            case (32, 0):
                // $script:0119135307007862$
                // - Ah, you must be quite content with your life. You're always welcome to visit if you need a place to rest and escape from reality.
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
