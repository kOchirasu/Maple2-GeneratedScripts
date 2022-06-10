using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003107: QuietMinds Guild Leader
/// </summary>
public class _11003107 : NpcScript {
    internal _11003107(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0119135307007855$ 
                // - There's nothing like a glass of something sweet to drink away your stress.
                return true;
            case 30:
                // $script:0119135307007858$ 
                // - Are you stressed out? I formed the QuietMinds guild to help people escape from the many stresses of life.
                switch (selection) {
                    // $script:0119135307007859$
                    // - I totally want to join your guild!
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0119135307007860$
                    // - Not really my scene, but thanks.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0119135307007861$ 
                // - Oh! I'm sorry, but my guild is already full. Hm... Well, I'm sure I'm not the only one who formed a guild to relax. There has to be another chill guild somewhere. Or you could start your own.
                return true;
            case 32:
                // $script:0119135307007862$ 
                // - Ah, you must be quite content with your life. You're always welcome to visit if you need a place to rest and escape from reality.
                return true;
            default:
                return true;
        }
    }
}
