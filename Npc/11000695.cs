using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000695: Bazette
/// </summary>
public class _11000695 : NpcScript {
    internal _11000695(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002802$ 
                // - What brings you here? 
                return true;
            case 50:
                // $script:0831180407002806$ 
                // - Making potions is very difficult. The first priority is preparing the ingredients. You need very specific ingredients to make effective potions. 
                // $script:0831180407002807$ 
                // - Some people compare potion brewing to cooking. They're crazy if they think potions are as easy to make as food. 
                // $script:0831180407002808$ 
                // - Here, I'll give you an example. Say you're making fried rice. You can put in just about anything you want. Ham, peppers, carrots, anything you want. 
                // $script:0831180407002809$ 
                // - When you're making a potion, however, you must add the ingredients in the correct order, at the correct time. You can't take your eyes off the cauldron. 
                return true;
            default:
                return true;
        }
    }
}
