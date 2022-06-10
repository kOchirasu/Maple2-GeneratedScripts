using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000806: Lepen
/// </summary>
public class _11000806 : NpcScript {
    internal _11000806(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002969$ 
                // - Is there something you want from me?
                return true;
            case 30:
                // $script:0831180407002972$ 
                // - So, you want to know where $item:20000046$ came from? Sure, I'll tell you. It's not like I have any reason to hide it now.
                // $script:0831180407002973$ 
                // - While I was making supplements in a corner of Goldus's drug factory, I accidentally came across a sample of $item:20000102$, a natural stimulant.
                // $script:0831180407002974$ 
                // - When ingested, this chemical heightens one's mood, relaxes their mind, and also gives an energy boost. The empire prohibited its use simply because it's produced in the Land of Darkness. All that did was drive the trade underground!
                return true;
            default:
                return true;
        }
    }
}
